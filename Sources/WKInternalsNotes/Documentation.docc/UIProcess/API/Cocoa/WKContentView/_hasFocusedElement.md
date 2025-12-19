# ``WKInternalsNotes/WKContentView/_hasFocusedElement()``

フォーカス中の要素が存在するかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_hasFocusedElement;
```

## Discussion
`_focusedElementInformation.elementType` が `InputType::None` かどうかで判定する。

## References
- [`WKContentViewInteraction.h#L768`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L768)
- [`WKContentViewInteraction.mm#L5423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L5423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
