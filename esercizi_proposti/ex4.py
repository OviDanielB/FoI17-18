"""
  * Esercizio 4
  * Scrivere una funzione ricorsiva in Python che, data un intero positivo n,
  * ritorna i coefficienti della riga n-esima del triangolo di Tartaglia.
  * Ad esempio, per n = 4, ritorna [1, 3, 3, 1].
  *
  * Qualche osservazione:
  *     - ogni riga del triangolo comincia e finisce con 1
  *     - tutti gli altri elementi della riga sono somma di due elementi della riga precedente
  *     - ripetere finche' non si arriva ad n = 1 e restituisce [1]
"""

def pascal(n):
# @param n: Int n-esima riga triangolo Tartaglia
    if n == 1:
        return [1]
    else:
        line = [1] # ogni riga comincia con 1
        previous_line = pascal(n-1) # ricorsione
        for i in range(len(previous_line) - 1):
            # somma elementi riga precedente
            line.append(previous_line[i] + previous_line[i+1])
        line += [1] # ogni riga finisce con 1
    return line
