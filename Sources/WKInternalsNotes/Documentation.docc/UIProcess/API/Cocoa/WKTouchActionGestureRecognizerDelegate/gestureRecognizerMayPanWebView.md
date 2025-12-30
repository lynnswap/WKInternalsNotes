# ``WKInternalsNotes/WKTouchActionGestureRecognizerDelegate/gestureRecognizerMayPanWebView(_:)``

WebView のパンを許可するジェスチャか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)gestureRecognizerMayPanWebView:(UIGestureRecognizer *)gestureRecognizer;
```

## Discussion
メイン `UIScrollView` の `panGestureRecognizer` または `WKChildScrollView` に紐づくパンジェスチャの場合に `YES` を返す。

## References
- [`WKTouchActionGestureRecognizer.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.h#L41)
- [`WKContentViewInteraction.mm#L2349`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2349)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
