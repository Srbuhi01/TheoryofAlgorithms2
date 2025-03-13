{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f9b14392",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "9\n",
      "8\n",
      "1\n",
      "7\n",
      "3\n",
      "2\n",
      "4\n",
      "5\n",
      "6\n",
      "10\n",
      "11\n"
     ]
    }
   ],
   "source": [
    "graph = {\n",
    "    0: [9],\n",
    "    1: [0],\n",
    "    2: [],\n",
    "    3: [2, 4, 5],\n",
    "    4: [],\n",
    "    5: [6],\n",
    "    6: [7],\n",
    "    7: [3, 10],\n",
    "    8: [1, 7],\n",
    "    9: [8],\n",
    "    10: [11],\n",
    "    11: [7],\n",
    "    12: []\n",
    "}\n",
    "\n",
    "visited = set()\n",
    "\n",
    "def DFS(graph, node, visited):\n",
    "    if node not in visited:\n",
    "        visited.add(node)\n",
    "        print(node)\n",
    "        \n",
    "        for neighbor in graph[node]:\n",
    "            DFS(graph, neighbor, visited)\n",
    "\n",
    "DFS(graph, 0 , visited)    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6028e132",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
