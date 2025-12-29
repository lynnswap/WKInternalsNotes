# ``WKInternalsNotes/WKARPresentationSession/currentFrame``

現在の `ARFrame` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, retain, readonly) ARFrame *currentFrame;
```

## Default Value
`ARSession` の `currentFrame`。

## Discussion
保持している `ARSession` から `currentFrame` を取得して返す。

## References
- [`WKARPresentationSession.mm#L179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L179)
- [`WKARPresentationSession.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
