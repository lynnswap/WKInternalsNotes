# ``WKInternalsNotes/WKARPresentationSession/renderingFrameIndex``

描画フレームのインデックスを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSUInteger renderingFrameIndex;
```

## Default Value
`0`。

## Discussion
`_loadMetal` で 0 に初期化され、`startFrame` でフレーム開始ごとに 1 加算される。

## References
- [`WKARPresentationSession.mm#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L143)
- [`WKARPresentationSession.mm#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L195)
- [`WKARPresentationSession.mm#L350`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L350)
- [`WKARPresentationSession.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
