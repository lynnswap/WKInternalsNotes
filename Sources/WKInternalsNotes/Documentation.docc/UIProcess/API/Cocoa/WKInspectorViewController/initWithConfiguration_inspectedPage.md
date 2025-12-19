# ``WKInternalsNotes/WKInspectorViewController/initWithConfiguration(_:inspectedPage:)``

Web Inspector 用ビューコントローラを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithConfiguration:(_WKInspectorConfiguration *)configuration inspectedPage:(NakedPtr<WebKit::WebPageProxy>)inspectedPage;
```

## Discussion
設定を `copy` して保持し、`inspectedPage` を `_inspectedPage` に保存する。Remote Inspector の場合は `inspectedPage` が `nil` になる。

## References
- [`WKInspectorViewController.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L47)
- [`WKInspectorViewController.mm#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.mm#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
