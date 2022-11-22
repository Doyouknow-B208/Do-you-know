package com.common.DoYouKnow.domain.entity;

import lombok.*;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor(access = AccessLevel.PROTECTED)
@Builder
public class DYKClubContent extends BaseEntity{
    private String type;
    private String content;


    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="dykclub_id")
    private DYKClub dykClub;

}
