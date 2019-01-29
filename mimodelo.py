class Ordenamientos(object):

    def Seleccion(self, A):
        for x in range(0, len(A) - 1):
            masP =x
            for d in range(x+1, len(A)):
                if A[d] < A[masP]:
                    masP = d
            if masP != x:
                temp = A[x]
                A[x] = A[masP]
                A[masP] = temp
        return A


    def Insercion(self, A):
        for x in range(1, len(A)):
            aux = A[x]
            pos = x
            while pos > 0 and A[pos - 1] > aux:
                A[pos] = A[pos - 1]
                pos = pos -1
            A[pos] = aux
        return A




