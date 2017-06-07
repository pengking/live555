{
  'target_defaults': {
    'conditions': [
      ['OS != "win"', {
        'defines': [
          '_LARGEFILE_SOURCE',
          '_FILE_OFFSET_BITS=64',
        ],
        'conditions': [
          ['OS=="solaris"', {
            'cflags': [ '-pthreads' ],
          }],
          ['OS not in "solaris android"', {
            'cflags': [ '-pthread' ],
          }],
        ],
      }],
    ],

    'link_settings': {
            'libraries': [
              'kernel32.lib',
              'user32.lib',
              'gdi32.lib',
              'winspool.lib',
              'comdlg32.lib',
              'advapi32.lib',
              'shell32.lib',
              'ole32.lib',
              'oleaut32.lib',
              'uuid.lib',
              'odbc32.lib',
              'odbccp32.lib',

              # comctl32 miss will result 
              # error LNK2019 unresolved external symbol __imp__InitCommonControls
              # ref http //bbs.csdn.net/topics/280070106

              'comctl32.lib',
              #'Riched20.lib',
            ],
          },
    'configurations': {
        'Debug': {
          'msvs_settings': {
              'VCCLCompilerTool': {
              # 多线程调试 DLL (/MD)
              'RuntimeLibrary': '2',
              # 不优化 /Od
              'Optimization': '0',
              'DebugInformationFormat': '4',
            },
            'VCLinkerTool': {
            'GenerateDebugInformation': 'true',
            'GenerateMapFile': 'false',
            'IgnoreDefaultLibraryNames': [
                #'Libcmtd.lib'
              ],
            },
          },
        }, # Debug

        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # 多线程 DLL (/MD)
              'RuntimeLibrary': '2',
              # 完全优化 /Os
              'Optimization': '2',
              # 使用内部函数 /Oi
              'EnableIntrinsicFunctions': 'true',
              # 程序数据库 (/Zi)
              'DebugInformationFormat': '3',
            },
            'VCLinkerTool': {
              'GenerateDebugInformation': 'true',
              'GenerateMapFile': 'false',

              'IgnoreDefaultLibraryNames': [
                #'Libcmtd.lib'
              ],
            },
          },
        }, # Release

      },
   
  },


  'targets': [

    # PROJECT PLUGIN TEST BEGIN 
    {
      'target_name':'live555',
      'type':'static_library',
      'include_dirs':[
        '../3rd/live555/UsageEnvironment/include',
        '../3rd/live555/groupsock/include',
        '../3rd/live555/liveMedia/include',
        '../3rd/live555/BasicUsageEnvironment/include',
      ],
      'sources':[
        
          '../3rd/live555/BasicUsageEnvironment/include/BasicHashTable.hh',
          '../3rd/live555/BasicUsageEnvironment/include/BasicUsageEnvironment.hh',
          '../3rd/live555/BasicUsageEnvironment/include/BasicUsageEnvironment0.hh',
          '../3rd/live555/BasicUsageEnvironment/include/BasicUsageEnvironment_version.hh',
          '../3rd/live555/BasicUsageEnvironment/include/DelayQueue.hh',
          '../3rd/live555/BasicUsageEnvironment/include/HandlerSet.hh',
          '../3rd/live555/groupsock/include/GroupEId.hh',
          '../3rd/live555/groupsock/include/Groupsock.hh',
          '../3rd/live555/groupsock/include/GroupsockHelper.hh',
          '../3rd/live555/groupsock/include/groupsock_version.hh',
          '../3rd/live555/groupsock/include/IOHandlers.hh',
          '../3rd/live555/groupsock/include/NetAddress.hh',
          '../3rd/live555/groupsock/include/NetCommon.h',
          '../3rd/live555/groupsock/include/NetInterface.hh',
          '../3rd/live555/groupsock/include/TunnelEncaps.hh',
          '../3rd/live555/liveMedia/EBMLNumber.hh',
          '../3rd/live555/liveMedia/H263plusVideoStreamParser.hh',
          '../3rd/live555/liveMedia/include/AC3AudioFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/AC3AudioRTPSink.hh',
          '../3rd/live555/liveMedia/include/AC3AudioRTPSource.hh',
          '../3rd/live555/liveMedia/include/AC3AudioStreamFramer.hh',
          '../3rd/live555/liveMedia/include/ADTSAudioFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/ADTSAudioFileSource.hh',
          '../3rd/live555/liveMedia/include/AMRAudioFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/AMRAudioFileSink.hh',
          '../3rd/live555/liveMedia/include/AMRAudioFileSource.hh',
          '../3rd/live555/liveMedia/include/AMRAudioRTPSink.hh',
          '../3rd/live555/liveMedia/include/AMRAudioRTPSource.hh',
          '../3rd/live555/liveMedia/include/AMRAudioSource.hh',
          '../3rd/live555/liveMedia/include/AudioInputDevice.hh',
          '../3rd/live555/liveMedia/include/AudioRTPSink.hh',
          '../3rd/live555/liveMedia/include/AVIFileSink.hh',
          '../3rd/live555/liveMedia/include/Base64.hh',
          '../3rd/live555/liveMedia/include/BasicUDPSink.hh',
          '../3rd/live555/liveMedia/include/BasicUDPSource.hh',
          '../3rd/live555/liveMedia/include/BitVector.hh',
          '../3rd/live555/liveMedia/include/ByteStreamFileSource.hh',
          '../3rd/live555/liveMedia/include/ByteStreamMemoryBufferSource.hh',
          '../3rd/live555/liveMedia/include/ByteStreamMultiFileSource.hh',
          '../3rd/live555/liveMedia/include/DeviceSource.hh',
          '../3rd/live555/liveMedia/include/DigestAuthentication.hh',
          '../3rd/live555/liveMedia/include/DVVideoFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/DVVideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/DVVideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/DVVideoStreamFramer.hh',
          '../3rd/live555/liveMedia/include/FileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/FileSink.hh',
          '../3rd/live555/liveMedia/include/FramedFileSource.hh',
          '../3rd/live555/liveMedia/include/FramedFilter.hh',
          '../3rd/live555/liveMedia/include/FramedSource.hh',
          '../3rd/live555/liveMedia/include/GenericMediaServer.hh',
          '../3rd/live555/liveMedia/include/GSMAudioRTPSink.hh',
          '../3rd/live555/liveMedia/include/H261VideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/H263plusVideoFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/H263plusVideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/H263plusVideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/H263plusVideoStreamFramer.hh',
          '../3rd/live555/liveMedia/include/H264or5VideoFileSink.hh',
          '../3rd/live555/liveMedia/include/H264or5VideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/H264or5VideoStreamDiscreteFramer.hh',
          '../3rd/live555/liveMedia/include/H264or5VideoStreamFramer.hh',
          '../3rd/live555/liveMedia/include/H264VideoFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/H264VideoFileSink.hh',
          '../3rd/live555/liveMedia/include/H264VideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/H264VideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/H264VideoStreamDiscreteFramer.hh',
          '../3rd/live555/liveMedia/include/H264VideoStreamFramer.hh',
          '../3rd/live555/liveMedia/include/H265VideoFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/H265VideoFileSink.hh',
          '../3rd/live555/liveMedia/include/H265VideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/H265VideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/H265VideoStreamDiscreteFramer.hh',
          '../3rd/live555/liveMedia/include/H265VideoStreamFramer.hh',
          '../3rd/live555/liveMedia/include/InputFile.hh',
          '../3rd/live555/liveMedia/include/JPEGVideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/JPEGVideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/JPEGVideoSource.hh',
          '../3rd/live555/liveMedia/include/liveMedia.hh',
          '../3rd/live555/liveMedia/include/liveMedia_version.hh',
          '../3rd/live555/liveMedia/include/Locale.hh',
          '../3rd/live555/liveMedia/include/MatroskaFile.hh',
          '../3rd/live555/liveMedia/include/MatroskaFileServerDemux.hh',
          '../3rd/live555/liveMedia/include/Media.hh',
          '../3rd/live555/liveMedia/include/MediaSession.hh',
          '../3rd/live555/liveMedia/include/MediaSink.hh',
          '../3rd/live555/liveMedia/include/MediaSource.hh',
          '../3rd/live555/liveMedia/include/MediaTranscodingTable.hh',
          '../3rd/live555/liveMedia/include/MP3ADU.hh',
          '../3rd/live555/liveMedia/include/MP3ADUinterleaving.hh',
          '../3rd/live555/liveMedia/include/MP3ADURTPSink.hh',
          '../3rd/live555/liveMedia/include/MP3ADURTPSource.hh',
          '../3rd/live555/liveMedia/include/MP3ADUTranscoder.hh',
          '../3rd/live555/liveMedia/include/MP3AudioFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/MP3FileSource.hh',
          '../3rd/live555/liveMedia/include/MP3Transcoder.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2AudioRTPSink.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2AudioRTPSource.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2AudioStreamFramer.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2Demux.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2DemuxedElementaryStream.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2DemuxedServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2FileServerDemux.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2VideoFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2VideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2VideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2VideoStreamDiscreteFramer.hh',
          '../3rd/live555/liveMedia/include/MPEG1or2VideoStreamFramer.hh',
          '../3rd/live555/liveMedia/include/MPEG2IndexFromTransportStream.hh',
          '../3rd/live555/liveMedia/include/MPEG2TransportFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/MPEG2TransportStreamFramer.hh',
          '../3rd/live555/liveMedia/include/MPEG2TransportStreamFromESSource.hh',
          '../3rd/live555/liveMedia/include/MPEG2TransportStreamFromPESSource.hh',
          '../3rd/live555/liveMedia/include/MPEG2TransportStreamIndexFile.hh',
          '../3rd/live555/liveMedia/include/MPEG2TransportStreamMultiplexor.hh',
          '../3rd/live555/liveMedia/include/MPEG2TransportStreamTrickModeFilter.hh',
          '../3rd/live555/liveMedia/include/MPEG2TransportUDPServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/MPEG4ESVideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/MPEG4ESVideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/MPEG4GenericRTPSink.hh',
          '../3rd/live555/liveMedia/include/MPEG4GenericRTPSource.hh',
          '../3rd/live555/liveMedia/include/MPEG4LATMAudioRTPSink.hh',
          '../3rd/live555/liveMedia/include/MPEG4LATMAudioRTPSource.hh',
          '../3rd/live555/liveMedia/include/MPEG4VideoFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/MPEG4VideoStreamDiscreteFramer.hh',
          '../3rd/live555/liveMedia/include/MPEG4VideoStreamFramer.hh',
          '../3rd/live555/liveMedia/include/MPEGVideoStreamFramer.hh',
          '../3rd/live555/liveMedia/include/MultiFramedRTPSink.hh',
          '../3rd/live555/liveMedia/include/MultiFramedRTPSource.hh',
          '../3rd/live555/liveMedia/include/OggFile.hh',
          '../3rd/live555/liveMedia/include/OggFileServerDemux.hh',
          '../3rd/live555/liveMedia/include/OggFileSink.hh',
          '../3rd/live555/liveMedia/include/OnDemandServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/ourMD5.hh',
          '../3rd/live555/liveMedia/include/OutputFile.hh',
          '../3rd/live555/liveMedia/include/PassiveServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/ProxyServerMediaSession.hh',
          '../3rd/live555/liveMedia/include/QCELPAudioRTPSource.hh',
          '../3rd/live555/liveMedia/include/QuickTimeFileSink.hh',
          '../3rd/live555/liveMedia/include/QuickTimeGenericRTPSource.hh',
          '../3rd/live555/liveMedia/include/RTCP.hh',
          '../3rd/live555/liveMedia/include/RTPInterface.hh',
          '../3rd/live555/liveMedia/include/RTPSink.hh',
          '../3rd/live555/liveMedia/include/RTPSource.hh',
          '../3rd/live555/liveMedia/include/RTSPClient.hh',
          '../3rd/live555/liveMedia/include/RTSPCommon.hh',
          '../3rd/live555/liveMedia/include/RTSPRegisterSender.hh',
          '../3rd/live555/liveMedia/include/RTSPServer.hh',
          '../3rd/live555/liveMedia/include/RTSPServerSupportingHTTPStreaming.hh',
          '../3rd/live555/liveMedia/include/ServerMediaSession.hh',
          '../3rd/live555/liveMedia/include/SimpleRTPSink.hh',
          '../3rd/live555/liveMedia/include/SimpleRTPSource.hh',
          '../3rd/live555/liveMedia/include/SIPClient.hh',
          '../3rd/live555/liveMedia/include/StreamReplicator.hh',
          '../3rd/live555/liveMedia/include/T140TextRTPSink.hh',
          '../3rd/live555/liveMedia/include/TCPStreamSink.hh',
          '../3rd/live555/liveMedia/include/TextRTPSink.hh',
          '../3rd/live555/liveMedia/include/TheoraVideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/TheoraVideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/uLawAudioFilter.hh',
          '../3rd/live555/liveMedia/include/VideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/VorbisAudioRTPSink.hh',
          '../3rd/live555/liveMedia/include/VorbisAudioRTPSource.hh',
          '../3rd/live555/liveMedia/include/VP8VideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/VP8VideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/VP9VideoRTPSink.hh',
          '../3rd/live555/liveMedia/include/VP9VideoRTPSource.hh',
          '../3rd/live555/liveMedia/include/WAVAudioFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/include/WAVAudioFileSource.hh',
          '../3rd/live555/liveMedia/MatroskaDemuxedTrack.hh',
          '../3rd/live555/liveMedia/MatroskaFileParser.hh',
          '../3rd/live555/liveMedia/MatroskaFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/MP3ADUdescriptor.hh',
          '../3rd/live555/liveMedia/MP3AudioMatroskaFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/MP3Internals.hh',
          '../3rd/live555/liveMedia/MP3InternalsHuffman.hh',
          '../3rd/live555/liveMedia/MP3StreamState.hh',
          '../3rd/live555/liveMedia/MPEGVideoStreamParser.hh',
          '../3rd/live555/liveMedia/OggDemuxedTrack.hh',
          '../3rd/live555/liveMedia/OggFileParser.hh',
          '../3rd/live555/liveMedia/OggFileServerMediaSubsession.hh',
          '../3rd/live555/liveMedia/rtcp_from_spec.h',
          '../3rd/live555/liveMedia/StreamParser.hh',
          '../3rd/live555/UsageEnvironment/include/Boolean.hh',
          '../3rd/live555/UsageEnvironment/include/HashTable.hh',
          '../3rd/live555/UsageEnvironment/include/strDup.hh',
          '../3rd/live555/UsageEnvironment/include/UsageEnvironment.hh',
          '../3rd/live555/UsageEnvironment/include/UsageEnvironment_version.hh',
          '../3rd/live555/BasicUsageEnvironment/BasicHashTable.cpp',
          '../3rd/live555/BasicUsageEnvironment/BasicTaskScheduler.cpp',
          '../3rd/live555/BasicUsageEnvironment/BasicTaskScheduler0.cpp',
          '../3rd/live555/BasicUsageEnvironment/BasicUsageEnvironment.cpp',
          '../3rd/live555/BasicUsageEnvironment/BasicUsageEnvironment0.cpp',
          '../3rd/live555/BasicUsageEnvironment/DelayQueue.cpp',
          '../3rd/live555/groupsock/GroupEId.cpp',
          '../3rd/live555/groupsock/Groupsock.cpp',
          '../3rd/live555/groupsock/GroupsockHelper.cpp',
          '../3rd/live555/groupsock/inet.c',
          '../3rd/live555/groupsock/IOHandlers.cpp',
          '../3rd/live555/groupsock/NetAddress.cpp',
          '../3rd/live555/groupsock/NetInterface.cpp',
          '../3rd/live555/liveMedia/AC3AudioFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/AC3AudioRTPSink.cpp',
          '../3rd/live555/liveMedia/AC3AudioRTPSource.cpp',
          '../3rd/live555/liveMedia/AC3AudioStreamFramer.cpp',
          '../3rd/live555/liveMedia/ADTSAudioFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/ADTSAudioFileSource.cpp',
          '../3rd/live555/liveMedia/AMRAudioFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/AMRAudioFileSink.cpp',
          '../3rd/live555/liveMedia/AMRAudioFileSource.cpp',
          '../3rd/live555/liveMedia/AMRAudioRTPSink.cpp',
          '../3rd/live555/liveMedia/AMRAudioRTPSource.cpp',
          '../3rd/live555/liveMedia/AMRAudioSource.cpp',
          '../3rd/live555/liveMedia/AudioInputDevice.cpp',
          '../3rd/live555/liveMedia/AudioRTPSink.cpp',
          '../3rd/live555/liveMedia/AVIFileSink.cpp',
          '../3rd/live555/liveMedia/Base64.cpp',
          '../3rd/live555/liveMedia/BasicUDPSink.cpp',
          '../3rd/live555/liveMedia/BasicUDPSource.cpp',
          '../3rd/live555/liveMedia/BitVector.cpp',
          '../3rd/live555/liveMedia/ByteStreamFileSource.cpp',
          '../3rd/live555/liveMedia/ByteStreamMemoryBufferSource.cpp',
          '../3rd/live555/liveMedia/ByteStreamMultiFileSource.cpp',
          '../3rd/live555/liveMedia/DeviceSource.cpp',
          '../3rd/live555/liveMedia/DigestAuthentication.cpp',
          '../3rd/live555/liveMedia/DVVideoFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/DVVideoRTPSink.cpp',
          '../3rd/live555/liveMedia/DVVideoRTPSource.cpp',
          '../3rd/live555/liveMedia/DVVideoStreamFramer.cpp',
          '../3rd/live555/liveMedia/EBMLNumber.cpp',
          '../3rd/live555/liveMedia/FileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/FileSink.cpp',
          '../3rd/live555/liveMedia/FramedFileSource.cpp',
          '../3rd/live555/liveMedia/FramedFilter.cpp',
          '../3rd/live555/liveMedia/FramedSource.cpp',
          '../3rd/live555/liveMedia/GenericMediaServer.cpp',
          '../3rd/live555/liveMedia/GSMAudioRTPSink.cpp',
          '../3rd/live555/liveMedia/H261VideoRTPSource.cpp',
          '../3rd/live555/liveMedia/H263plusVideoFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/H263plusVideoRTPSink.cpp',
          '../3rd/live555/liveMedia/H263plusVideoRTPSource.cpp',
          '../3rd/live555/liveMedia/H263plusVideoStreamFramer.cpp',
          '../3rd/live555/liveMedia/H263plusVideoStreamParser.cpp',
          '../3rd/live555/liveMedia/H264or5VideoFileSink.cpp',
          '../3rd/live555/liveMedia/H264or5VideoRTPSink.cpp',
          '../3rd/live555/liveMedia/H264or5VideoStreamDiscreteFramer.cpp',
          '../3rd/live555/liveMedia/H264or5VideoStreamFramer.cpp',
          '../3rd/live555/liveMedia/H264VideoFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/H264VideoFileSink.cpp',
          '../3rd/live555/liveMedia/H264VideoRTPSink.cpp',
          '../3rd/live555/liveMedia/H264VideoRTPSource.cpp',
          '../3rd/live555/liveMedia/H264VideoStreamDiscreteFramer.cpp',
          '../3rd/live555/liveMedia/H264VideoStreamFramer.cpp',
          '../3rd/live555/liveMedia/H265VideoFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/H265VideoFileSink.cpp',
          '../3rd/live555/liveMedia/H265VideoRTPSink.cpp',
          '../3rd/live555/liveMedia/H265VideoRTPSource.cpp',
          '../3rd/live555/liveMedia/H265VideoStreamDiscreteFramer.cpp',
          '../3rd/live555/liveMedia/H265VideoStreamFramer.cpp',
          '../3rd/live555/liveMedia/InputFile.cpp',
          '../3rd/live555/liveMedia/JPEGVideoRTPSink.cpp',
          '../3rd/live555/liveMedia/JPEGVideoRTPSource.cpp',
          '../3rd/live555/liveMedia/JPEGVideoSource.cpp',
          '../3rd/live555/liveMedia/Locale.cpp',
          '../3rd/live555/liveMedia/MatroskaDemuxedTrack.cpp',
          '../3rd/live555/liveMedia/MatroskaFile.cpp',
          '../3rd/live555/liveMedia/MatroskaFileParser.cpp',
          '../3rd/live555/liveMedia/MatroskaFileServerDemux.cpp',
          '../3rd/live555/liveMedia/MatroskaFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/Media.cpp',
          '../3rd/live555/liveMedia/MediaSession.cpp',
          '../3rd/live555/liveMedia/MediaSink.cpp',
          '../3rd/live555/liveMedia/MediaSource.cpp',
          '../3rd/live555/liveMedia/MP3ADU.cpp',
          '../3rd/live555/liveMedia/MP3ADUdescriptor.cpp',
          '../3rd/live555/liveMedia/MP3ADUinterleaving.cpp',
          '../3rd/live555/liveMedia/MP3ADURTPSink.cpp',
          '../3rd/live555/liveMedia/MP3ADURTPSource.cpp',
          '../3rd/live555/liveMedia/MP3ADUTranscoder.cpp',
          '../3rd/live555/liveMedia/MP3AudioFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/MP3AudioMatroskaFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/MP3FileSource.cpp',
          '../3rd/live555/liveMedia/MP3Internals.cpp',
          '../3rd/live555/liveMedia/MP3InternalsHuffman.cpp',
          '../3rd/live555/liveMedia/MP3InternalsHuffmanTable.cpp',
          '../3rd/live555/liveMedia/MP3StreamState.cpp',
          '../3rd/live555/liveMedia/MP3Transcoder.cpp',
          '../3rd/live555/liveMedia/MPEG1or2AudioRTPSink.cpp',
          '../3rd/live555/liveMedia/MPEG1or2AudioRTPSource.cpp',
          '../3rd/live555/liveMedia/MPEG1or2AudioStreamFramer.cpp',
          '../3rd/live555/liveMedia/MPEG1or2Demux.cpp',
          '../3rd/live555/liveMedia/MPEG1or2DemuxedElementaryStream.cpp',
          '../3rd/live555/liveMedia/MPEG1or2DemuxedServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/MPEG1or2FileServerDemux.cpp',
          '../3rd/live555/liveMedia/MPEG1or2VideoFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/MPEG1or2VideoRTPSink.cpp',
          '../3rd/live555/liveMedia/MPEG1or2VideoRTPSource.cpp',
          '../3rd/live555/liveMedia/MPEG1or2VideoStreamDiscreteFramer.cpp',
          '../3rd/live555/liveMedia/MPEG1or2VideoStreamFramer.cpp',
          '../3rd/live555/liveMedia/MPEG2IndexFromTransportStream.cpp',
          '../3rd/live555/liveMedia/MPEG2TransportFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/MPEG2TransportStreamFramer.cpp',
          '../3rd/live555/liveMedia/MPEG2TransportStreamFromESSource.cpp',
          '../3rd/live555/liveMedia/MPEG2TransportStreamFromPESSource.cpp',
          '../3rd/live555/liveMedia/MPEG2TransportStreamIndexFile.cpp',
          '../3rd/live555/liveMedia/MPEG2TransportStreamMultiplexor.cpp',
          '../3rd/live555/liveMedia/MPEG2TransportStreamTrickModeFilter.cpp',
          '../3rd/live555/liveMedia/MPEG2TransportUDPServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/MPEG4ESVideoRTPSink.cpp',
          '../3rd/live555/liveMedia/MPEG4ESVideoRTPSource.cpp',
          '../3rd/live555/liveMedia/MPEG4GenericRTPSink.cpp',
          '../3rd/live555/liveMedia/MPEG4GenericRTPSource.cpp',
          '../3rd/live555/liveMedia/MPEG4LATMAudioRTPSink.cpp',
          '../3rd/live555/liveMedia/MPEG4LATMAudioRTPSource.cpp',
          '../3rd/live555/liveMedia/MPEG4VideoFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/MPEG4VideoStreamDiscreteFramer.cpp',
          '../3rd/live555/liveMedia/MPEG4VideoStreamFramer.cpp',
          '../3rd/live555/liveMedia/MPEGVideoStreamFramer.cpp',
          '../3rd/live555/liveMedia/MPEGVideoStreamParser.cpp',
          '../3rd/live555/liveMedia/MultiFramedRTPSink.cpp',
          '../3rd/live555/liveMedia/MultiFramedRTPSource.cpp',
          '../3rd/live555/liveMedia/OggDemuxedTrack.cpp',
          '../3rd/live555/liveMedia/OggFile.cpp',
          '../3rd/live555/liveMedia/OggFileParser.cpp',
          '../3rd/live555/liveMedia/OggFileServerDemux.cpp',
          '../3rd/live555/liveMedia/OggFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/OggFileSink.cpp',
          '../3rd/live555/liveMedia/OnDemandServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/ourMD5.cpp',
          '../3rd/live555/liveMedia/OutputFile.cpp',
          '../3rd/live555/liveMedia/PassiveServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/ProxyServerMediaSession.cpp',
          '../3rd/live555/liveMedia/QCELPAudioRTPSource.cpp',
          '../3rd/live555/liveMedia/QuickTimeFileSink.cpp',
          '../3rd/live555/liveMedia/QuickTimeGenericRTPSource.cpp',
          '../3rd/live555/liveMedia/RTCP.cpp',
          '../3rd/live555/liveMedia/rtcp_from_spec.c',
          '../3rd/live555/liveMedia/RTPInterface.cpp',
          '../3rd/live555/liveMedia/RTPSink.cpp',
          '../3rd/live555/liveMedia/RTPSource.cpp',
          '../3rd/live555/liveMedia/RTSPClient.cpp',
          '../3rd/live555/liveMedia/RTSPCommon.cpp',
          '../3rd/live555/liveMedia/RTSPRegisterSender.cpp',
          '../3rd/live555/liveMedia/RTSPServer.cpp',
          '../3rd/live555/liveMedia/RTSPServerRegister.cpp',
          '../3rd/live555/liveMedia/RTSPServerSupportingHTTPStreaming.cpp',
          '../3rd/live555/liveMedia/ServerMediaSession.cpp',
          '../3rd/live555/liveMedia/SimpleRTPSink.cpp',
          '../3rd/live555/liveMedia/SimpleRTPSource.cpp',
          '../3rd/live555/liveMedia/SIPClient.cpp',
          '../3rd/live555/liveMedia/StreamParser.cpp',
          '../3rd/live555/liveMedia/StreamReplicator.cpp',
          '../3rd/live555/liveMedia/T140TextRTPSink.cpp',
          '../3rd/live555/liveMedia/TCPStreamSink.cpp',
          '../3rd/live555/liveMedia/TextRTPSink.cpp',
          '../3rd/live555/liveMedia/TheoraVideoRTPSink.cpp',
          '../3rd/live555/liveMedia/TheoraVideoRTPSource.cpp',
          '../3rd/live555/liveMedia/uLawAudioFilter.cpp',
          '../3rd/live555/liveMedia/VideoRTPSink.cpp',
          '../3rd/live555/liveMedia/VorbisAudioRTPSink.cpp',
          '../3rd/live555/liveMedia/VorbisAudioRTPSource.cpp',
          '../3rd/live555/liveMedia/VP8VideoRTPSink.cpp',
          '../3rd/live555/liveMedia/VP8VideoRTPSource.cpp',
          '../3rd/live555/liveMedia/VP9VideoRTPSink.cpp',
          '../3rd/live555/liveMedia/VP9VideoRTPSource.cpp',
          '../3rd/live555/liveMedia/WAVAudioFileServerMediaSubsession.cpp',
          '../3rd/live555/liveMedia/WAVAudioFileSource.cpp',
          '../3rd/live555/UsageEnvironment/HashTable.cpp',
          '../3rd/live555/UsageEnvironment/strDup.cpp',
          '../3rd/live555/UsageEnvironment/UsageEnvironment.cpp',


      ],
      'link_settings':{
        'libraries':[
        ]
      },
      'defines':[
        'WIN32',
        'NDEBUG',
        '_WINDOWS',
        'UILIB_EXPORTS',
        #'_UNICODE',
        #'UNICODE',
       ],

    },

    # PROJECT PLUGIN TEST END




    # BEGIN ROC PROJECT

     {
      'target_name':'roc',
      'type':'executable',
      'include_dirs':[
        '../3rd/live555/BasicUsageEnvironment/include',
        '../3rd/live555/groupsock/include',
        '../3rd/live555/liveMedia/include',
        '../3rd/live555/UsageEnvironment/include',
        '../3rd',
      ],
      'sources':[
          '../roc/log.cpp',
          '../roc/session.cpp',
          '../roc/server.cpp',
          '../roc/roc.cpp',
          '../3rd/spdlog/async_logger.h',
          '../3rd/spdlog/common.h',
          '../3rd/spdlog/details/async_logger_impl.h',
          '../3rd/spdlog/details/async_log_helper.h',
          '../3rd/spdlog/details/file_helper.h',
          '../3rd/spdlog/details/logger_impl.h',
          '../3rd/spdlog/details/log_msg.h',
          '../3rd/spdlog/details/mpmc_bounded_q.h',
          '../3rd/spdlog/details/null_mutex.h',
          '../3rd/spdlog/details/os.h',
          '../3rd/spdlog/details/pattern_formatter_impl.h',
          '../3rd/spdlog/details/registry.h',
          '../3rd/spdlog/details/spdlog_impl.h',
          '../3rd/spdlog/fmt/fmt.h',
          '../3rd/spdlog/fmt/ostr.h',
          '../3rd/spdlog/formatter.h',
          '../3rd/spdlog/logger.h',
          '../3rd/spdlog/sinks/android_sink.h',
          '../3rd/spdlog/sinks/ansicolor_sink.h',
          '../3rd/spdlog/sinks/base_sink.h',
          '../3rd/spdlog/sinks/dist_sink.h',
          '../3rd/spdlog/sinks/file_sinks.h',
          '../3rd/spdlog/sinks/msvc_sink.h',
          '../3rd/spdlog/sinks/null_sink.h',
          '../3rd/spdlog/sinks/ostream_sink.h',
          '../3rd/spdlog/sinks/sink.h',
          '../3rd/spdlog/sinks/stdout_sinks.h',
          '../3rd/spdlog/sinks/syslog_sink.h',
          '../3rd/spdlog/spdlog.h',
          '../3rd/spdlog/tweakme.h',
          '../roc/log.h',
          '../roc/session.h',
          '../roc/server.h',
      ],
      'link_settings':{
        'libraries':[
        'ws2_32.lib',
        './Release/lib/live555.lib'
        ]
      },
      'defines':[
        'WIN32',
        'NDEBUG',
        '_WINDOWS',
        'UILIB_EXPORTS',
       ],

    },
    # END ROC PROJECT

        # BEGIN ROC PROJECT

     {
      'target_name':'servertest',
      'type':'executable',
      'include_dirs':[
        '../3rd/live555/BasicUsageEnvironment/include',
        '../3rd/live555/groupsock/include',
        '../3rd/live555/liveMedia/include',
        '../3rd/live555/UsageEnvironment/include',
        '../3rd',
      ],
      'sources':[
          '../example/main.cpp',
      ],
      'link_settings':{
        'libraries':[
        'ws2_32.lib',
        './Release/lib/live555.lib'
        ]
      },
      'defines':[
        'WIN32',
        'NDEBUG',
        '_WINDOWS',
        'UILIB_EXPORTS',
       ],

    },
    # END ROC PROJECT

    # BEGIN ROC PROJECT

     {
      'target_name':'rtspserver',
      'type':'executable',
      'include_dirs':[
        '../3rd/live555/BasicUsageEnvironment/include',
        '../3rd/live555/groupsock/include',
        '../3rd/live555/liveMedia/include',
        '../3rd/live555/UsageEnvironment/include',
        '../3rd',
      ],
      'sources':[
          '../example/rtspserver/DynamicRTSPServer.cpp', 
          '../example/rtspserver/DynamicRTSPServer.hh', 
          '../example/rtspserver/live555MediaServer.cpp', 
          '../example/rtspserver/version.hh', 
      ],
      'link_settings':{
        'libraries':[
        'ws2_32.lib',
        './Release/lib/live555.lib'
        ]
      },
      'defines':[
        'WIN32',
        'NDEBUG',
        '_WINDOWS',
        'UILIB_EXPORTS',
       ],

    },
    # END RTSPSERVER TEST


    # BEGIN MY RTSPSERVER TEST

     {
      'target_name':'TestRtspServer',
      'type':'executable',
      'include_dirs':[
        '../3rd/live555/BasicUsageEnvironment/include',
        '../3rd/live555/groupsock/include',
        '../3rd/live555/liveMedia/include',
        '../3rd/live555/UsageEnvironment/include',
        '../3rd',
      ],
      'sources':[
          '../example/TestRtspServer/TestRtspServer.cpp', 
          '../example/TestRtspServer/TestRtspServer.h', 
          '../example/TestRtspServer/main.cpp',  
      ],
      'link_settings':{
        'libraries':[
        'ws2_32.lib',
        './Release/lib/live555.lib'
        ]
      },
      'defines':[
        'WIN32',
        'NDEBUG',
        '_WINDOWS',
        'UILIB_EXPORTS',
       ],

    },
    # END MY RTSPSERVER TEST





  ]
}
