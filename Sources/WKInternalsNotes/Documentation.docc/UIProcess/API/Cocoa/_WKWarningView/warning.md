# ``WKInternalsNotes/_WKWarningView/warning``

表示対象の `BrowsingWarning` を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) RefPtr<const WebKit::BrowsingWarning> warning;
```

## Default Value
`initWithFrame:browsingWarning:completionHandler:` で設定される。

## Discussion
初期化時に `_warning` に参照を保持し、以降は `warning` から参照される。

## References
- [`_WKWarningView.h#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/_WKWarningView.h#L78)
- [`_WKWarningView.mm#L314`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/_WKWarningView.mm#L314)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
