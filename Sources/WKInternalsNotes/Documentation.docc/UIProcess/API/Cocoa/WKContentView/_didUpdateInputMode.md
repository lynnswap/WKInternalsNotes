# ``WKInternalsNotes/WKContentView/_didUpdateInputMode(_:)``

入力モード更新を反映する。

## Objective-C Declaration
```objective-c
- (void)_didUpdateInputMode:(WebCore::InputMode)mode;
```

## Discussion
`inputDelegate` が無い、またはフォーカス要素が無い場合は何もしない。watchOS 以外では `inputMode` を更新して `reloadInputViews` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L813`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L813)
- [`WKContentViewInteraction.mm#L8750`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8750)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
