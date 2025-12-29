# ``WKInternalsNotes/_WKAutomationSessionConfiguration/suppressesICECandidateFiltering``

ICE Candidate のフィルタリング抑制を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL suppressesICECandidateFiltering;
```

## Default Value
`NO`。

## Discussion
`init` で `NO` に初期化され、`copyWithZone:` で現在の値が複製される。

## References
- [`_WKAutomationSessionConfiguration.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.h#L37)
- [`_WKAutomationSessionConfiguration.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.mm#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
