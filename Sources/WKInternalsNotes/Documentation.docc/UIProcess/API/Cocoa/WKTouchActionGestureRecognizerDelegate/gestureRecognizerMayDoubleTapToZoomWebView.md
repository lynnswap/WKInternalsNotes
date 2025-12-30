# ``WKInternalsNotes/WKTouchActionGestureRecognizerDelegate/gestureRecognizerMayDoubleTapToZoomWebView(_:)``

ダブルタップズームを許可するジェスチャか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)gestureRecognizerMayDoubleTapToZoomWebView:(UIGestureRecognizer *)gestureRecognizer;
```

## Discussion
`_doubleTapGestureRecognizer` または `_twoFingerDoubleTapGestureRecognizer` と一致する場合に `YES` を返す。

## References
- [`WKTouchActionGestureRecognizer.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.h#L43)
- [`WKContentViewInteraction.mm#L2378`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2378)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
