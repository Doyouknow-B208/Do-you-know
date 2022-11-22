package com.common.DoYouKnow.dto;

import com.common.DoYouKnow.domain.entity.Keyword;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.format.annotation.DateTimeFormat;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;

@NoArgsConstructor
@AllArgsConstructor
@Builder
@Data
public class KeywordResponse {
    private Long id;
    private String name;
    @DateTimeFormat(pattern = "yyyy-MM-dd")
    private Date date;
    private int count;


    public static KeywordResponse response(Keyword k) {
        return KeywordResponse.builder().id(k.getId()).date(k.getDate()).name(k.getName()).count(k.getCount()).build();
    }
}
