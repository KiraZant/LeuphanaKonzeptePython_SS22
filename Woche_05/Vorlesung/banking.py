import bankaccounts as ba

acc = ba.Konto(1, "J", "DE12")
dep = ba.Depotkonto([], 0, "J", "DE98")

dep.einzahlen(100)