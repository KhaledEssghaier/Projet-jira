package com.example.microservice_hi.repository;

import com.example.microservice_hi.model.Favori;
import org.springframework.data.mongodb.repository.MongoRepository;
import java.util.List;

public interface FavoriRepository extends MongoRepository<Favori, String> {
    List<Favori> findByUserId(String userId);
    boolean existsByUserIdAndFormationId(String userId, String formationId);
    void deleteByUserIdAndFormationId(String userId, String formationId);
}