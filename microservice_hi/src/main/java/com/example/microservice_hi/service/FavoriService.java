package com.example.microservice_hi.service;

import com.example.microservice_hi.model.Favori;
import java.util.List;

public interface FavoriService {
    Favori addFavori(Favori favori);
    void removeFavori(String userId, String formationId);
    List<Favori> getUserFavoris(String userId);
}