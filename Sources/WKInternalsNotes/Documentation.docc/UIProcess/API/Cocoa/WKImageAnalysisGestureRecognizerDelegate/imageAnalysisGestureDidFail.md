# ``WKInternalsNotes/WKImageAnalysisGestureRecognizerDelegate/imageAnalysisGestureDidFail(_:)``

画像解析ジェスチャ失敗時の後始末を行う。

## Objective-C Declaration
```objective-c
- (void)imageAnalysisGestureDidFail:(WKImageAnalysisGestureRecognizer *)gesture;
```

## Discussion
`WKContentView` 側の実装では `_endImageAnalysisGestureDeferral:` を呼び出し、ジェスチャ抑制を行わずに終了させる。

## References
- [`WKImageAnalysisGestureRecognizer.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKImageAnalysisGestureRecognizer.h#L36)
- [`WKContentViewInteraction.mm#L13308`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13308)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
