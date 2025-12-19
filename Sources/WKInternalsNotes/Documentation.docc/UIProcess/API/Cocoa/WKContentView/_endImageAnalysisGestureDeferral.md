# ``WKInternalsNotes/WKContentView/_endImageAnalysisGestureDeferral(_:)``

画像解析ジェスチャのデファリングを終了する。

## Objective-C Declaration
```objective-c
- (void)_endImageAnalysisGestureDeferral:(WebKit::ShouldPreventGestures)shouldPreventGestures;
```

## Discussion
`_imageAnalysisDeferringGestureRecognizer` に `endDeferral` を通知する。

## References
- [`WKContentViewInteraction.h#L980`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L980)
- [`WKContentViewInteraction.mm#L12533`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12533)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
