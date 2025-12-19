# ``WKInternalsNotes/WKScrollView/_setInternalTopPocketColor(_:)``

内部用のトップポケット色を設定する。

## Objective-C Declaration
```objective-c
- (void)_setInternalTopPocketColor:(UIColor *)color;
```

## Discussion
内部で保持している色が変わった場合に更新し、`_updateTopPocketColor` を呼んで反映する。

## References
- [`WKScrollView.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L60)
- [`WKScrollView.mm#L665`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L665)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
