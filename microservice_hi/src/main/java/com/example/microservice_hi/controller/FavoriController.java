package com.example.microservice_hi.controller;

import com.example.microservice_hi.model.Favori;
import com.example.microservice_hi.service.FavoriService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/favoris")
public class FavoriController {
    private final FavoriService favoriService;

    public FavoriController(FavoriService favoriService) {
        this.favoriService = favoriService;
    }

    @PostMapping
    public Favori addFavori(@RequestBody Favori favori) {
        return favoriService.addFavori(favori);
    }

    @DeleteMapping("/{userId}/{formationId}")
    public void removeFavori(@PathVariable String userId,
                             @PathVariable String formationId) {
        favoriService.removeFavori(userId, formationId);
    }

    @GetMapping("/{userId}")
    public List<Favori> getUserFavoris(@PathVariable String userId) {
        return favoriService.getUserFavoris(userId);
    }
}