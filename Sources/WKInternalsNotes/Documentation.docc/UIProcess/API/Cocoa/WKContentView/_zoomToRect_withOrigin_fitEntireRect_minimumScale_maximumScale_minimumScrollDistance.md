# ``WKInternalsNotes/WKContentView/_zoomToRect(_:withOrigin:fitEntireRect:minimumScale:maximumScale:minimumScrollDistance:)``

指定矩形へのズームとスクロールを実行する。

## Objective-C Declaration
```objective-c
- (BOOL)_zoomToRect:(CGRect)targetRect withOrigin:(CGPoint)origin fitEntireRect:(BOOL)fitEntireRect minimumScale:(double)minimumScale maximumScale:(double)maximumScale minimumScrollDistance:(CGFloat)minimumScrollDistance;
```

## Discussion
`WKWebView` の `_zoomToRect:withOrigin:fitEntireRect:minimumScale:maximumScale:minimumScrollDistance:` を呼び、ズーム可否の結果を返す。

## References
- [`WKContentView.h#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L135)
- [`WKContentView.mm#L1067`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1067)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
