'''CREATED BY JAVIER MOYANO SAN BRUNO (100495884) AND
    JORGE MEJIAS DONOSO (100495807), 27-03-2023'''

import random
from slistH import SList
from slistH import SNode
import sys


class SList2(SList):

    def del_largest_seq(self):
        'Borramos la secuencia mas larga'

        #vemos si la lista esta vacia
        if self.isEmpty():
            print("Empty")
            return
        #vemos si solo hay uno
        if self._size == 1:
            self.removeLast()
            print("Empty")
            return

        #Establecemos una seria de contadores para localizar las secuencias
        node_it = self._head
        cont_ant = 0
        cont_pos = 0
        pos = 0
        while node_it:
            next_node = node_it.next
            cont = 0
            found = False
            #buscamos la secuencia mas larga
            while not found:
                if next_node is None:
                    if cont >= cont_ant:
                        cont_ant = cont
                        pos = cont_pos
                    found = True

                elif node_it.elem == next_node.elem:
                    next_node = next_node.next
                    cont += 1

                else:
                    if cont >= cont_ant:
                        cont_ant = cont
                        pos = cont_pos

                    found = True

            node_it = next_node
            if cont == 0:
                cont_pos += 1
            else:
                cont_pos += cont + 1

        #borramos la secuenia mas larga
        node = self._head
        next_node = self._head
        index = pos + cont_ant + 1
        for j in range(index):
            if j == (pos - 1):
                node = next_node
            if (pos - 1) < j < index:
                self._size -= 1
            next_node = next_node.next

        node.next = next_node


    def fix_loop(self):
        if self.isEmpty():      #Si la lista esta vacia termina del proceso
            print("Error: la lista está vacía")
            return False
        else:
            node_it = self._head
            if node_it.next is None:
                return False
            else:
                contador = 2
                node_aux = node_it.next
                while node_aux.next is not None:        #Se comprueban los nodos de despues del principal
                    node_it = self._head
                    for n in range(contador):       #El contador marca cuantos nodos se analizan dependiendo del lugar de la lista donde se encuentre el bucle
                        if node_aux.next == node_it:
                            node_aux.next = None
                            return True
                        else:
                            node_it = node_it.next      #Si no hay bucle se pasa al siguiente

                    node_aux = node_aux.next
                    contador += 1
                return False

    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next
        current.next = start_node

    def left_right_shift(self, left, n):
        '''Este metodo mueve los n numero del principio al final o viceversa'''
        if n >= self._size or n <= 0: #se acaba si n mayor o menor que el tamaño de la lista
            return

        if type(left) != bool: #si no es booleano
            return

        first_node = self._head  #declaramos 2 nodos en la cabeza
        last_node = self._head

        for _ in range(self._size - 1): #cogemos el ultimo nodo
            last_node = last_node.next
        prev = self._head

        if left: #principio al final
            for _ in range(n - 1): #cogemos el ultimo nodo que se va a mover del inicio
                prev = prev.next

        else: #final al principio
            for _ in range(self._size - n - 1): #cogemos el ultimo nodo que
                # se va a mover del final
                prev = prev.next

        #establecemos la cabeza en el siguiente
        self._head = prev.next
        #el primero nodo lo enlazamos al ultimos
        last_node.next = first_node
        prev.next = None
