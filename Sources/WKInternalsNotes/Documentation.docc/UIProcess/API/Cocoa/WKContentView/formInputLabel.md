# ``WKInternalsNotes/WKContentView/formInputLabel``

フォーム入力ラベル文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *formInputLabel;
```

## Default Value
`PEPPER_UI_CORE` が無効な環境では `nil`。

## Discussion
`PEPPER_UI_CORE` が有効な場合は、`_presentedFullScreenInputViewController` に対する `inputLabelTextForViewController:` の結果を返す。

## References
- [`WKContentViewInteraction.h#L1063`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1063)
- [`WKContentViewInteraction.mm#L14544`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14544)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
