package com.newbrank.service.impl;

import com.newbrank.model.Videos;
import com.newbrank.mapper.VideosMapper;
import com.newbrank.service.MPVideosService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 *  服务实现类
 * </p>
 *
 * @author christopher
 * @since 2020-11-19
 */
@Service
public class VideosServiceImpl extends ServiceImpl<VideosMapper, Videos> implements MPVideosService {

}
