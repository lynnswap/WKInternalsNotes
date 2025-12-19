# ``WKInternalsNotes/WKContentView/buildMenuForWebViewWithBuilder(_:)``

WebView 用のメニュー構成を追加する。

## Objective-C Declaration
```objective-c
- (void)buildMenuForWebViewWithBuilder:(id <UIMenuBuilder>)builder;
```

## Discussion
機能フラグに応じて、背景削除や App Highlight、スクロール・トゥ・テキスト・フラグメント用のメニューを挿入する。

## References
- [`WKContentViewInteraction.h#L755`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L755)
- [`WKContentViewInteraction.mm#L12106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12106)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
