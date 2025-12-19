# ``WKInternalsNotes/WKContentView/_targetContentZoomScaleForRect(_:currentScale:fitEntireRect:minimumScale:maximumScale:)``

指定矩形に対するターゲットズーム倍率を計算する。

## Objective-C Declaration
```objective-c
- (double)_targetContentZoomScaleForRect:(const WebCore::FloatRect&)targetRect currentScale:(double)currentScale fitEntireRect:(BOOL)fitEntireRect minimumScale:(double)minimumScale maximumScale:(double)maximumScale;
```

## Discussion
`WKWebView` の `_targetContentZoomScaleForRect:currentScale:fitEntireRect:minimumScale:maximumScale:` に委譲する。

## References
- [`WKContentView.h#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L140)
- [`WKContentView.mm#L1092`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1092)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
