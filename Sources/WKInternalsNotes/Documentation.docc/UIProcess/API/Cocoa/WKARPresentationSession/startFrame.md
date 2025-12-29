# ``WKInternalsNotes/WKARPresentationSession/startFrame()``

フレーム開始処理を行う。

## Objective-C Declaration
```objective-c
- (NSUInteger)startFrame;
```

## Discussion
`currentFrame` を取得できない場合は 0 を返す。取得できた場合は `capturedImage` と `nextDrawable` を取得し、`renderingFrameIndex` を更新して 1 を返す。

## References
- [`WKARPresentationSession.mm#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L195)
- [`WKARPresentationSession.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
