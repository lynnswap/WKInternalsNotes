# ``WKInternalsNotes/WKContentView/didZoomToScale(_:)``

ズーム完了時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)didZoomToScale:(CGFloat)scale;
```

## Discussion
`scale` は使用せず、`_didEndScrollingOrZooming` を呼び出す。

## References
- [`WKContentView.h#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L88)
- [`WKContentView.mm#L761`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L761)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
