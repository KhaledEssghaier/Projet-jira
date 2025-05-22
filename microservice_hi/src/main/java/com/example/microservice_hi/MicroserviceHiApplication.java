package com.example.microservice_hi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@SpringBootApplication
@EnableCaching
public class MicroserviceHiApplication {
	public static void main(String[] args) {
		SpringApplication.run(MicroserviceHiApplication.class, args);
	}
}