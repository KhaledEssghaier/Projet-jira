package com.example.microservice_hi.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "favoris")
public class Favori {
    @Id
    private String id;
    private String userId;
    private String formationId;

    // Constructeurs, getters et setters
}