# ``WKInternalsNotes/WKContentView/_setTransform3DForModelViews(_:)``

モデル表示のスケール変更を通知する。

## Objective-C Declaration
```objective-c
- (void)_setTransform3DForModelViews:(CGFloat)newScale;
```

## Discussion
`modelPresentationManagerProxy` が存在する場合に `pageScaleDidChange` を呼び出す。

## References
- [`WKContentView.h#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L142)
- [`WKContentView.mm#L1098`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1098)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
