# ``WKInternalsNotes/WKTouchActionGestureRecognizerDelegate/gestureRecognizerMayPinchToZoomWebView(_:)``

ピンチズームを許可するジェスチャか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)gestureRecognizerMayPinchToZoomWebView:(UIGestureRecognizer *)gestureRecognizer;
```

## Discussion
メイン `UIScrollView` の `pinchGestureRecognizer` なら `YES`。その他の `UIPinchGestureRecognizer` は `UIDelegate` の `_webView:gestureRecognizerCouldPinch:` があればその結果を返す。

## References
- [`WKTouchActionGestureRecognizer.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.h#L42)
- [`WKContentViewInteraction.mm#L2362`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2362)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
