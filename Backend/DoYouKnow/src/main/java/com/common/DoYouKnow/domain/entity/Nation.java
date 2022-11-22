package com.common.DoYouKnow.domain.entity;

import lombok.*;
import org.springframework.format.annotation.DateTimeFormat;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.OneToMany;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * 유저 모델 정의.
 */
@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor(access = AccessLevel.PROTECTED)
@Builder
public class Nation extends BaseEntity{
    @Column(unique = true)
    private String name;
    private String code;
    private String twitter_code;
    private String language;

    @OneToMany(mappedBy = "nation")
    private List<Keyword> keywords = new ArrayList<>();
}