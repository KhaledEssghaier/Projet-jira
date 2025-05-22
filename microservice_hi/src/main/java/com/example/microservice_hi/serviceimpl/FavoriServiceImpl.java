package com.example.microservice_hi.serviceimpl;

import com.example.microservice_hi.model.Favori;
import com.example.microservice_hi.repository.FavoriRepository;
import com.example.microservice_hi.service.FavoriService;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class FavoriServiceImpl implements FavoriService {
    private final FavoriRepository favoriRepository;

    public FavoriServiceImpl(FavoriRepository favoriRepository) {
        this.favoriRepository = favoriRepository;
    }

    @Override
    public Favori addFavori(Favori favori) {
        return favoriRepository.save(favori);
    }

    @Override
    @CacheEvict(value = "favoris", key = "#userId")
    public void removeFavori(String userId, String formationId) {
        favoriRepository.deleteByUserIdAndFormationId(userId, formationId);
    }

    @Override
    @Cacheable(value = "favoris", key = "#userId")
    public List<Favori> getUserFavoris(String userId) {
        return favoriRepository.findByUserId(userId);
    }
}