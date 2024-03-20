from tqdm import tqdm

def check_gpu_torch(num_iterations=5000, num_elements=10000):
    import torch
    """
    Checks GPU usage by performing a computationally intensive matrix multiplication task.

    Args:
        num_iterations (int, optional): The number of iterations to perform the matrix
            multiplication (default: 1000). Higher values will increase computation time and
            GPU usage for better visualization.
        num_elements (int, optional): The size of the matrices involved in the
            multiplication (default: 100000). Larger matrices will consume more memory and
            potentially increase GPU utilization.

    Prints information about GPU availability, device, memory usage, and utilization.
    """

    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("GPU is available!")
        print("Using device:", device)

        # Create large matrices on the GPU
        a = torch.randn(num_elements, num_elements, device=device)
        b = torch.randn(num_elements, num_elements, device=device)

        # Perform computationally intensive matrix multiplication
        for _ in tqdm(range(num_iterations)):
            c = torch.matmul(a, b)


        # Get current GPU memory usage
        memory_allocated = torch.cuda.memory_allocated(device=device) / (1024 ** 3)  # Convert to GB
        memory_cached = torch.cuda.torch.cuda.max_memory_reserved(device=device) / (1024 ** 3)  # Convert to GB

        print("GPU memory usage:", f"{memory_allocated:.2f} GB allocated, {memory_cached:.2f} GB cached")

        # Get GPU utilization (requires Nvidia System Management Interface (nvidia-smi) tool)
        # Uncomment the following lines if you want to try getting GPU utilization,
        # but be aware that it might not work on all systems
        # import psutil
        # gpu_utilization = psutil.get_gpu_memory_info().utilized / 100
        # print("GPU utilization:", f"{gpu_utilization:.2f}%")
    else:
        print("GPU is not available.")

def check_gpu_tf(iterations=1000):
    import tensorflow as tf
    """Performs a computationally expensive task to check GPU usage."""

    with tf.device('/GPU:0'):  # Explicitly assign operations to the first GPU
        matrix_size = 20
        matrix_a = tf.random.normal(shape=(matrix_size, matrix_size))
        matrix_b = tf.random.normal(shape=(matrix_size, matrix_size))

        for _ in tqdm(range(iterations)):
            # Perform a matrix multiplication operation
            matrix_c = tf.matmul(matrix_a, matrix_b)

    # Use tf.config.list_physical_devices('GPU') to verify actual GPU usage
    physical_devices = tf.config.list_physical_devices('GPU')
    if physical_devices:
        print('GPU(s) are available.')
    else:
        print('No GPU(s) are available.')


if __name__ == "__main__":
    # check_gpu_tf()
    check_gpu_torch()

