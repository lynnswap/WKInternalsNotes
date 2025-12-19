# ``WKInternalsNotes/WKInspectorViewController/webView``

Inspector 用の `WKWebView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKWebView *webView;
```

## Discussion
初回アクセス時に `WKInspectorWKWebView` を生成し、UI/ナビゲーション/Inspector delegate を設定する。safe area 変更を監視して `obscuredContentInsets` を更新する。

## References
- [`WKInspectorViewController.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L44)
- [`WKInspectorViewController.mm#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.mm#L104)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
