# ``WKInternalsNotes/_WKWebAuthenticationPanel/delegate``

パネルの delegate を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, weak) id <_WKWebAuthenticationPanelDelegate> delegate;
```

## Default Value
未設定の場合は `nil`。

## Discussion
getter は `WebAuthenticationPanelClient` の delegate を返す。setter は `WebAuthenticationPanelClient` を生成して `_client` に保持し、`API::WebAuthenticationPanel` に設定する。

## References
- [`_WKWebAuthenticationPanel.h#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L132)
- [`_WKWebAuthenticationPanel.mm#L168`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L168)
- [`_WKWebAuthenticationPanel.mm#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L176)
- [`_WKWebAuthenticationPanel.mm#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L178)
- [`_WKWebAuthenticationPanel.mm#L180`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L180)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
