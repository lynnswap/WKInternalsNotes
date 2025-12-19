# ``WKInternalsNotes/WKPageHostedModelView/setPortalCrossing(_:)``

ポータル通過の有効/無効を設定する。

## Objective-C Declaration
```objective-c
- (void)setPortalCrossing:(BOOL)enabled;
```

## Discussion
ステレオコンテンツ有効時に `REPortalCrossingFlagsComponent` のフラグを更新し、dirty をマークする。

## References
- [`WKPageHostedModelView.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPageHostedModelView.h#L38)
- [`WKPageHostedModelView.mm#L301`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPageHostedModelView.mm#L301)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
