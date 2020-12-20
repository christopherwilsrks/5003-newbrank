package com.newbrank.service.impl;

import com.newbrank.model.Channel;
import com.newbrank.mapper.ChannelMapper;
import com.newbrank.service.MPChannelService;
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
public class ChannelServiceImpl extends ServiceImpl<ChannelMapper, Channel> implements MPChannelService {

}
