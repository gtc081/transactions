import json
from classes.violations import *
from datetime import datetime

class Main:
    def __init__(self):
        self.activate_card = False
        self.account = False
        self.limit = 0
        self.violations = []
        self.transactions = []
        self.transactions_printed = []

    def check_account(self, line):
        if self.activate_card:
            self.violations.append(AAI)
        else:
            self.account = True
            self.activate_card = bool(line['active-card'])
            self.limit = int(line["available-limit"])

    def convert_epoch(self, t):
        utc_time = datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%fZ")
        epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
        return int(epoch_time)

    def check_HFSI(self, l):
        c = 0
        for i in self.transactions:
            if l['time'] - i['time'] <= 120:
                c+=1
        return c

    def check_DT(self, l):
        c = 0
        for i in self.transactions:
            if l['time'] - i['time'] <= 120 and l['merchant']==i['merchant'] and l['amount'] == i['amount']:
                c+=1
        return c

    def check_transaction(self, line):

        t = self.convert_epoch(line['time'])
        line['time'] = t

        if not self.account:
            self.violations.append(ANI)
            return
        if not self.activate_card:
            self.violations.append(CNA)
            return
        if int(line['amount']) > self.limit:
            self.violations.append(IL)
        if self.check_HFSI(line)>=3:
            self.violations.append(HFSI)
        if self.check_DT(line)>=1:
            self.violations.append(DT)

        if len(self.violations) == 0:
            self.limit = self.limit - int(line['amount'])
            self.transactions.append(line)

    def add_line(self):
        if not self.account:
            a = {}
        else:
            a = {
                    "active-card": self.activate_card,
                    "available-limit": self.limit
                }
        r = {
                "account":a, 
                "violations":self.violations
            }
        self.transactions_printed.append(json.dumps(r))

    def check_lines(self, line):
        try:
            l = json.loads(line)
            if "account" in l:
                self.check_account(l['account'])
                self.add_line()
            elif "transaction" in l:
                self.check_transaction(l['transaction'])
                self.add_line()
            else:
                print("ERRO: JSON sem informação de \"account\" ou de \"transaction\"")
                raise
            self.violations = []
        except json.decoder.JSONDecodeError:
            print("ERRO: linha não está no formato JSON adequado")

    def check_ops(self, lines):
        for i in lines:
            self.check_lines(i)

    def print_lines(self):
        for i in self.transactions_printed:
            print(i)