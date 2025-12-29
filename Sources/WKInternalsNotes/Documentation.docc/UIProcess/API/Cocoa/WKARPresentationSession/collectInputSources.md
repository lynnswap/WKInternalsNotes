# ``WKInternalsNotes/WKARPresentationSession/collectInputSources()``

入力ソースを収集して返す。

## Objective-C Declaration
```objective-c
- (Vector<PlatformXR::FrameData::InputSource>)collectInputSources;
```

## Discussion
`_WKTransientGestureRecognizer` から input sources を取得して返す。

## References
- [`WKARPresentationSession.mm#L210`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L210)
- [`WKARPresentationSession.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
