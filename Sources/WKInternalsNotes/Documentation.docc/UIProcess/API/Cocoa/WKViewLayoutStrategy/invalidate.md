# ``WKInternalsNotes/WKViewLayoutStrategy/invalidate()``

保持しているページ/ビュー参照を破棄する。

## Objective-C Declaration
```objective-c
- (void)invalidate;
```

## Discussion
`_page` と `_webViewImpl` を `nullptr` にし、`_view` を `nil` にする。

## References
- [`WKViewLayoutStrategy.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L90)
- [`WKViewLayoutStrategy.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.h#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
