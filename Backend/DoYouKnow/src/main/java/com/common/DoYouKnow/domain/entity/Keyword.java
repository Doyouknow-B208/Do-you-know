package com.common.DoYouKnow.domain.entity;

import lombok.*;
import org.springframework.format.annotation.DateTimeFormat;

import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;

/**
 * 유저 모델 정의.
 */
@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor(access = AccessLevel.PROTECTED)
@Builder
public class Keyword extends BaseEntity {
    private String name;
    @DateTimeFormat(pattern = "yyyy-MM-dd")
    private Date date;
    private int count;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="nation_id")
    private Nation nation;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="category_id")
    private Category category;
}