# ``WKInternalsNotes/WKContentView/_zoomToFocusRect(_:selectionRect:fontSize:minimumScale:maximumScale:allowScaling:forceScroll:)``

指定矩形へのズームを実行する。

## Objective-C Declaration
```objective-c
- (void)_zoomToFocusRect:(CGRect)rectToFocus selectionRect:(CGRect)selectionRect fontSize:(float)fontSize minimumScale:(double)minimumScale maximumScale:(double)maximumScale allowScaling:(BOOL)allowScaling forceScroll:(BOOL)forceScroll;
```

## Discussion
`WKWebView` の `_zoomToFocusRect:selectionRect:fontSize:minimumScale:maximumScale:allowScaling:forceScroll:` に引き継ぎ、ズーム対象矩形やスケール制約を渡す。

## References
- [`WKContentView.h#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L134)
- [`WKContentView.mm#L1056`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1056)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
