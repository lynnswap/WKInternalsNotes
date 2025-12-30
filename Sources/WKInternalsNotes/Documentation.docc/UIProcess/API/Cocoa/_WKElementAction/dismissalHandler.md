# ``WKInternalsNotes/_WKElementAction/dismissalHandler``

アクション実行後にシートを閉じるか判定するハンドラ。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) WKElementActionDismissalHandler dismissalHandler;
```

## Default Value
`nil`。

## Discussion
`WKActionSheetAssistant` が `shouldDismissHandler` で参照し、`nil` の場合は常に閉じる。Data Detectors のアクションでは UI 表示の有無に応じて設定される。

## References
- [`_WKElementAction.h#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L83)
- [`WKActionSheetAssistant.mm#L364`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L364)
- [`WKActionSheetAssistant.mm#L753`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L753)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
