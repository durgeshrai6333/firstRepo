package com.example.todo.repository;

import com.example.todo.model.Todo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository // Optional, but good practice for Spring to recognize it as a bean
public interface TodoRepository extends JpaRepository<Todo, Long> {
    // JpaRepository already provides CRUD methods:
    // save(), findById(), findAll(), deleteById(), etc.
    // No custom methods needed for now.
}
