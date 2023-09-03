{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO8lUnOTnTleZjscmWDPDeh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/savino365/lab1_CMPS6100/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 105
        },
        "id": "sqKl2DW0GUnf",
        "outputId": "0f81feb1-dc0e-4aeb-9cdf-96d22682168e"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'\\n#########    #########\\n### Test Functions ###\\n#########    #########\\n\\n# You can run them on the terminal.\\n# The command:\\n#\\n# pytest main.py::test_is_divisible_by\\n#\\n# Will run the test_is_divisible_by test function.\\n\\ndef test_is_divisible_by():\\n    assert is_divisible_by(2, 2) == True\\n    assert is_divisible_by(3, 2) == False\\n    assert is_divisible_by(47, 7) == False\\n\\ndef test_is_prime():\\n    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 241, 461, 701, 881, 883, 997]\\n    for prime in primes:\\n        assert is_prime(prime) == True\\n    composites = [4, 6, 8, 9, 10, 25, 30, 36, 39, 49, 60, 64, 121]\\n    for composite in composites:\\n        assert is_prime(composite) == False\\n\\ndef test_count_primes():\\n    assert count_primes(10) == 4\\n    assert count_primes(100) == 25\\n    assert count_primes(1000) == 168\\n    assert count_primes(10000) == 1229\\n\\ndef test_count_twin_primes():\\n    assert count_twin_primes(10) == 2\\n    # The two pairs less than 10 are (3,5) and (5,7)\\n    assert count_twin_primes(100) == 8\\n    assert count_twin_primes(1000) == 35\\n    assert count_twin_primes(10000) == 205'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 85
        }
      ],
      "source": [
        "\"\"\"\n",
        "CMPS 6100  Lab 1\n",
        "Author: Nicholas Savino\n",
        "\"\"\"\n",
        "\n",
        "### the only imports needed are here\n",
        "import math\n",
        "import time\n",
        "###\n",
        "\n",
        "def is_divisible_by(num, i):\n",
        "  # TO-DO\n",
        "  # Implement this function\n",
        "  if num % i == 0:\n",
        "    divisible = True\n",
        "  else:\n",
        "    divisible = False\n",
        "  return divisible\n",
        "\n",
        "def is_prime(num):\n",
        "  # TO-DO\n",
        "  # Implement this function\n",
        "  prime = True # assume the number is prime\n",
        "  if num <= 1: # 0 and negative numbers are neither prime nor composite\n",
        "    print('Choose a positive value. Numbers less than or equal to zero are neither prime nor composite')\n",
        "    prime = False\n",
        "  elif num % 1 != 0: #prevent the selection of non integer values\n",
        "    print('Choose an integer. Non integers are neither prime nor composite.')\n",
        "    prime = False\n",
        "  elif num == 4: #special case\n",
        "    prime = False\n",
        "  else:\n",
        "    for i in range (2,(num//2)):\n",
        "      if is_divisible_by(num,i) == True: #must have the is_diviseble func pre defined\n",
        "        prime = False #checks to see if num had divisors\n",
        "        break\n",
        "      else:\n",
        "        prime = True\n",
        "  return prime\n",
        "\n",
        "def generate_primes(upper_bound):\n",
        "  # TO-DO\n",
        "  # Implement this function\n",
        "  prime_list = []\n",
        "  i = 2\n",
        "  while i < upper_bound:\n",
        "    if is_prime(i) == True: #must have the is_prime func pre defined\n",
        "      prime_list.append(i)\n",
        "      i += 1\n",
        "    else:\n",
        "      i += 1\n",
        "  return(prime_list)\n",
        "\n",
        "\n",
        "def count_primes(upper_bound):\n",
        "  # TO-DO\n",
        "  # Implement this function\n",
        "  prime_list = generate_primes(upper_bound) #count the length of the list of primes, need to have the generate_primes func defined in advance\n",
        "  return(len(prime_list))\n",
        "\n",
        "x = 500000\n",
        "def generate_twin_primes(upper_bound):\n",
        "  # TO-DO\n",
        "  # Implement this function\n",
        "  twin_primes_list = [] #empty list\n",
        "  prime_list = generate_primes(upper_bound) #generate list of primes, need to have generate_primes func pre defined\n",
        "  j = 0\n",
        "  while j < len(prime_list)-1: #iterate through list of primes\n",
        "    if prime_list[j] == prime_list[j+1] - 2: #check to see if primes are seperated by 2\n",
        "      twin_primes_set_list = [] #empty list\n",
        "      twin_primes_set_list.append(prime_list[j]) #create list of two twin primes\n",
        "      twin_primes_set_list.append(prime_list[j+1]) #create list of two twin primes\n",
        "      twin_primes_list.append(twin_primes_set_list) #create list of list if twin prime pairs\n",
        "      j += 1\n",
        "    else:\n",
        "      j += 1\n",
        "  return(twin_primes_list)\n",
        "\n",
        "def count_twin_primes(upper_bound):\n",
        "  # TO-DO\n",
        "  # Implement this function\n",
        "  twin_primes_list = generate_twin_primes(upper_bound) #count the length of the list of twin primes, need to have the generate_twin_primes func defined in advance\n",
        "  return(len(twin_primes_list))\n",
        "\n",
        "'''\n",
        "start = time.time()\n",
        "generate_twin_primes(x)\n",
        "end = time.time()\n",
        "elapsed_time_ms = (end - start)*1000\n",
        "print('Elapsed Time: {:.2f} milliseconds'.format(elapsed_time_ms))\n",
        "'''\n",
        "\n",
        "'''\n",
        "#########    #########\n",
        "### Test Functions ###\n",
        "#########    #########\n",
        "\n",
        "# You can run them on the terminal.\n",
        "# The command:\n",
        "#\n",
        "# pytest main.py::test_is_divisible_by\n",
        "#\n",
        "# Will run the test_is_divisible_by test function.\n",
        "\n",
        "def test_is_divisible_by():\n",
        "    assert is_divisible_by(2, 2) == True\n",
        "    assert is_divisible_by(3, 2) == False\n",
        "    assert is_divisible_by(47, 7) == False\n",
        "\n",
        "def test_is_prime():\n",
        "    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 241, 461, 701, 881, 883, 997]\n",
        "    for prime in primes:\n",
        "        assert is_prime(prime) == True\n",
        "    composites = [4, 6, 8, 9, 10, 25, 30, 36, 39, 49, 60, 64, 121]\n",
        "    for composite in composites:\n",
        "        assert is_prime(composite) == False\n",
        "\n",
        "def test_count_primes():\n",
        "    assert count_primes(10) == 4\n",
        "    assert count_primes(100) == 25\n",
        "    assert count_primes(1000) == 168\n",
        "    assert count_primes(10000) == 1229\n",
        "\n",
        "def test_count_twin_primes():\n",
        "    assert count_twin_primes(10) == 2\n",
        "    # The two pairs less than 10 are (3,5) and (5,7)\n",
        "    assert count_twin_primes(100) == 8\n",
        "    assert count_twin_primes(1000) == 35\n",
        "    assert count_twin_primes(10000) == 205'''"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ZWH-GkeT531a"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}