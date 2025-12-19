# ``WKInternalsNotes/WKPageHostedModelView/applyBackgroundColor(_:)``

背景色をモデル表示に反映する。

## Objective-C Declaration
```objective-c
- (void)applyBackgroundColor:(std::optional<WebCore::Color>)backgroundColor;
```

## Discussion
ステレオコンテンツ有効時は埋め込みコンポーネントの clear color を更新する。無効時は `separatedOptions.material.clearColor` に白または指定色を設定する。

## References
- [`WKPageHostedModelView.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPageHostedModelView.h#L37)
- [`WKPageHostedModelView.mm#L256`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPageHostedModelView.mm#L256)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
