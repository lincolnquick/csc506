"""
hash_table.py

CSC 506 - Design and Analysis of Algorithms
Colorado State University Global Campus

Lincoln Quick
Feb 16, 2025

Description:
    This script implements a content recommendation system using hash tables.
    Two collision resolution strategies are implemented:
        1. Double Hashing (Open Addressing)
        2. Chaining (Linked List)

    The system simulates a social media platform where users interact with
    content. The hash tables store user-content interactions, allowing fast
    retrieval of recommended content for each user.

Sections:
    1. Define Hash Table Implementations
    2. Define Content Recommendation System
    3. Simulate User-Content Interactions
    4. Display Results

Output:
    - Inserts simulated user-content interactions.
    - Retrieves and displays recommended content for users.
"""
import random

class HashTableDoubleHashing:
    """
    Hash table implementation using double hashing for collision resolution.
    Stores user interactions with content for a recommendation system.
    """
    def __init__(self, size=101):
        self.size = size  # Prime number size for better hashing
        self.table = [None] * size
        self.prime = self._find_previous_prime(size)  # Secondary hash prime
    
    def _hash_primary(self, key):
        """Primary hash function."""
        return key % self.size
    
    def _hash_secondary(self, key):
        """Secondary hash function to avoid clustering."""
        return self.prime - (key % self.prime)
    
    def _find_previous_prime(self, n):
        """Finds the largest prime number less than n for secondary hashing."""
        for num in range(n - 1, 1, -1):
            if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
                return num
        return 3  # Default fallback
    
    def insert(self, user_id, content_id):
        """Inserts a user-content interaction into the hash table."""
        index = self._hash_primary(user_id)
        step = self._hash_secondary(user_id)
        
        while self.table[index] is not None:
            if self.table[index][0] == user_id:  # Update existing user
                self.table[index][1].add(content_id)
                return
            index = (index + step) % self.size  # Double hashing step
        
        self.table[index] = (user_id, {content_id})
    
    def get_recommendations(self, user_id):
        """Retrieves content recommendations for a user based on past interactions."""
        index = self._hash_primary(user_id)
        step = self._hash_secondary(user_id)
        
        while self.table[index] is not None:
            if self.table[index][0] == user_id:
                return list(self.table[index][1])  # Return list of content items
            index = (index + step) % self.size
        
        return []  # Return empty list if user not found

# Alternative: Hash Table with Chaining
class HashTableChaining:
    """
    Hash table using separate chaining (linked list) for collision resolution.
    """
    def __init__(self, size=101):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Simple modulo hash function."""
        return key % self.size
    
    def insert(self, user_id, content_id):
        """Inserts a user-content interaction into the hash table."""
        index = self._hash(user_id)
        for entry in self.table[index]:
            if entry[0] == user_id:
                entry[1].add(content_id)
                return
        self.table[index].append((user_id, {content_id}))
    
    def get_recommendations(self, user_id):
        """Retrieves content recommendations for a user."""
        index = self._hash(user_id)
        for entry in self.table[index]:
            if entry[0] == user_id:
                return list(entry[1])
        return []

# Testing the Hash Tables
if __name__ == "__main__":
    users = [101, 102, 103, 104]
    contents = ["Article1", "Article2", "Video1", "Video2"]
    
    # Double Hashing Implementation
    hash_table_dh = HashTableDoubleHashing()
    for _ in range(10):  # Simulating multiple interactions
        user = random.choice(users)
        content = random.choice(contents)
        hash_table_dh.insert(user, content)
    
    print("Double Hashing Recommendations:")
    for user in users:
        print(f"User {user}: {hash_table_dh.get_recommendations(user)}")
    
    # Chaining Implementation
    hash_table_ch = HashTableChaining()
    for _ in range(10):
        user = random.choice(users)
        content = random.choice(contents)
        hash_table_ch.insert(user, content)
    
    print("\nChaining Recommendations:")
    for user in users:
        print(f"User {user}: {hash_table_ch.get_recommendations(user)}")
