def file_operation(file, operation, data=None):
    """
    Perform file operations based on the specified mode.

    Parameters:
      file (str): The name of the file to operate on.
      operation (str): The mode of operation ('r' for read or 'w' for write).
      data (list, optional): The data to write to the file. Defaults to None.
    Returns:
      list: The data read from the file, if operation is 'r'.
    Raises:
      ValueError: If operation is not 'r' or 'w'.
    """
    with open(file, operation) as f:
        if operation == 'r':
            return f.readlines()
        elif operation == 'w':
            f.writelines(data)
        else:
            raise ValueError("Unsupported operation. Use 'r' for read or 'w' for write.")
