from SearchAlgorithms import *

def main():
    # List of unsorted numbers.
    # inputList = [6, 14, 5, 21, -9, -16, 87, 12, 8, 127, -5, 65]

    # List of sorted Strings (Cars).
    inputList = ['Alfa Romeo', 'BMW', 'Cadilac', 'Dodge', 'GMC', 'Honda', 'Marcedes', 'Toyota']

    # Print the unsorted list.
    # print('Input List of Numbers: ', numList)
    print('Input List : ', inputList)

    while True:
        print('Enter "Exit" to exit............')

        # item to be search.
        item = input('Enter item to search: ')

        if item == 'Exit':
            break

        # Desired Searching Algotithm.
        # index = indexOfItem(inputList, int(item))
        index = indexOfItem(inputList, item)

        # Print the Search Result.
        if index < 0:
            print('The {} is not found.'.format(item))
        else:
            print('The {} is position {} in the dataset.'.format(item, index))

    
if __name__ == '__main__':
    main()